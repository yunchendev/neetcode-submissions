class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_stack = deque(students)
        sandwich_stack = deque(sandwiches)

        attempts = 0
        while sandwich_stack and student_stack:
            if student_stack[0] == sandwich_stack[0]:
                student_stack.popleft()
                sandwich_stack.popleft()
                attempts = 0
            else:
                student_stack.append(student_stack.popleft())
                attempts += 1
            
            if attempts == len(student_stack):
                break

        return len(student_stack)