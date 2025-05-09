import turtle

def draw_tree(t, branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth == 0:
        return

    # Draw the branch
    t.forward(branch_length)
    
    # Left branch
    t.left(left_angle)
    draw_tree(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    t.right(left_angle)  # Restore original heading

    # Right branch
    t.right(right_angle)
    draw_tree(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    t.left(right_angle)  # Restore original heading

    # Move back to previous branch
    t.backward(branch_length)

def main():
    # Get user input
    left_angle = float(input("Enter left branch angle (degrees): "))
    right_angle = float(input("Enter right branch angle (degrees): "))
    start_length = float(input("Enter starting branch length: "))
    max_depth = int(input("Enter recursion depth: "))
    reduction_factor = float(input("Enter branch length reduction factor (e.g. 0.7): "))

    # Set up the turtle
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)  # Point upwards
    t.up()
    t.goto(0, -screen.window_height() // 2 + 20)
    t.down()

    # Started toDraw the tree
    draw_tree(t, start_length, left_angle, right_angle, max_depth, reduction_factor)

    # Finish
    turtle.done()

if __name__ == "__main__":
    main()
