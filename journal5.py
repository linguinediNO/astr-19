import numpy as np

def main():
    x = np.linspace(0.0, 2.0 * np.pi, 1000)

    print("sin(x) vs. x")
    print("x   sin(x)")

    for x in x:
        print(x, np.sin(x))

if __name__ == "__main__":
    main()