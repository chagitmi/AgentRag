class ResponseNode:

    def generate_response(self, worker_result):

        if worker_result["found"]:

            return (
                f"מצאתי את הנכס המבוקש.\n\n"
                f"קובץ: {worker_result['image_path']}\n"
                f"רמת התאמה: {worker_result['similarity']:.2f}"
            )

        return "לא מצאתי נכס מתאים במאגר."

    def generate_clarification(self):

        return (
            "לא הצלחתי להבין בדיוק מה דרוש.\n"
            "האם התכוונת ללוגו, חתימת מייל, כרטיס ביקור או מסמך רשמי?"
        )