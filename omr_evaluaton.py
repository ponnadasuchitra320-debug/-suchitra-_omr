import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found at: {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return thresh, image

def find_bubbles(thresh):
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bubbles = []
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        aspect_ratio = w / float(h)
        # Filter bubbles: adjust these based on your sheet!
        if 15 < w < 50 and 15 < h < 50 and 0.7 < aspect_ratio < 1.3:
            bubbles.append((x, y, w, h, c))
    if len(bubbles) == 0:
        raise ValueError("No bubbles detected. Check image quality or adjust filter parameters.")
    return bubbles

def sort_bubbles(bubbles):
    # Sort bubbles row-wise, then left to right
    bubbles.sort(key=lambda b: (b[1], b[0])) # sort by y, then x
    return bubbles

def group_bubbles_by_question(bubbles, questions=10, options=4):
    # Assumes uniform rows per question; requires adjustment for other layouts
    assert len(bubbles) >= questions * options, "Not enough bubbles detected for given questions and options."
    groups = []
    for q in range(questions):
        start_idx = q * options
        end_idx = start_idx + options
        group = bubbles[start_idx:end_idx]
        group.sort(key=lambda b: b[0]) # left-right for each question
        groups.append(group)
    return groups

def get_marked_answers(thresh, groups):
    marked_answers = {}
    for qidx, group in enumerate(groups):
        max_fill = -1
        selected = None
        for oidx, (x, y, w, h, c) in enumerate(group):
            mask = np.zeros(thresh.shape, dtype="uint8")
            cv2.drawContours(mask, [c], -1, 255, -1)
            filled = cv2.countNonZero(cv2.bitwise_and(thresh, thresh, mask=mask))
            if filled > max_fill:
                max_fill = filled
                selected = oidx
        marked_answers[qidx + 1] = selected
    return marked_answers

def score_answers(marked_answers, answer_key):
    score = 0
    results = {}
    for q, correct in answer_key.items():
        marked = marked_answers.get(q)
        results[q] = {'marked': marked, 'correct': correct, 'correctly_marked': marked == correct}
        if marked == correct:
            score += 1
    return score, results

if __name__ == "__main__":
    image_path = "path_to_your_omr_image.jpg" # Update to your file

    # Example: 10 questions, 4 options (index 0-based; adjust per actual sheet!)
    answer_key = {
        1: 0,
        2: 2,
        3: 1,
        4: 3,
        5: 0,
        6: 1,
        7: 2,
        8: 1,
        9: 3,
        10: 0
    }

    questions = len(answer_key)
    options = 4

    try:
        thresh, image = preprocess_image(image_path)
        bubbles = find_bubbles(thresh)
        bubbles = sort_bubbles(bubbles)
        groups = group_bubbles_by_question(bubbles, questions=questions, options=options)
        marked_answers = get_marked_answers(thresh, groups)
        score, results = score_answers(marked_answers, answer_key)

        print(f"Score: {score} out of {questions}\n")
        print("Details per question:")
        for q, info in results.items():
            print(f"Q{q}: Marked={info['marked']} | Correct={info['correct']} | {'✔' if info['correctly_marked'] else '✘'}")

    except Exception as e:
        print("Error:", e)
