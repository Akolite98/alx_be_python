from polymorphism_demo import Shape, Rectangle, Circle

def main():
    # Create a list of shape instances
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Iterate over the shapes and calculate their area
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
