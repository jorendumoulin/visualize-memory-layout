from visualize_matrix import visualize_strided_4d_layout


size = {
    'K': 16,
    'M': 16,
    'k': 4,
    'm': 4
}

strides = {
    'K': 64,
    'M': 4,
    'k': 16,
    'm': 1
}


# Visualize the matrix
visualize_strided_4d_layout(size, strides)
