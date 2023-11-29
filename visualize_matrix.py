import numpy as np
import matplotlib.pyplot as plt


def visualize_strided_4d_layout(matrix_size, strides):
    result_array = np.zeros((matrix_size["M"], matrix_size["K"]))

    # apply strided layout mapping
    for M in range(matrix_size["M"] // matrix_size["m"]):
        for K in range(matrix_size["K"] // matrix_size["k"]):
            for m in range(matrix_size["m"]):
                for k in range(matrix_size["k"]):
                    result_array[matrix_size["m"] * M + m][matrix_size["m"] * K + k] = (
                        strides["M"] * M
                        + strides["K"] * K
                        + strides["m"] * m
                        + strides["k"] * k
                    )

    visualize_matrix(result_array)


def visualize_matrix(matrix):
    """
    Visualizes a 2D matrix as a grid with a color scale and annotations.

    Parameters:
    - matrix: The 2D matrix to be visualized.
    """
    fig, ax = plt.subplots()

    # Display the matrix as a grid with a color scale
    im = ax.imshow(matrix, cmap="nipy_spectral", aspect="auto")

    # Add text annotations for each cell in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            text = f"{matrix[i, j]:.0f}"
            ax.text(j, i, text, ha="center", va="center", color="w")

    # Add a colorbar
    # cbar = ax.figure.colorbar(im, ax=ax)

    plt.savefig("result.png")


if __name__ == "__main__":
    # Example usage
    # Generate a random 2D matrix
    random_matrix = np.round(np.random.rand(16, 16) * 16 * 16)

    # Visualize the matrix
    visualize_matrix(random_matrix)
