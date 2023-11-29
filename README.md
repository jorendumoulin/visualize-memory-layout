# Visualize Memory Layout

A simple tool to visualize datalayout mappings for a 2D matrix using a 4D-tiled-matrix strided layout like this

![Result of the visualization.](/result.png)

The matrix is represented as follows:

```
                K
  +--------------------------+
  |       k                  |
  |   +-------+              |
  |   |       |              |
  | m |       |              |
  |   |       |              |
  |   +-------+              |
  |                          |
M |                          |
  |                          |
  |                          |
  |                          |
  |                          |
  |                          |
  |                          |
  +--------------------------+
```

For a 16x16 matrix with a tile size of 4x4, M=16, K=16, m=4, k=4

The size of the matrix must be specified with a dict

```python
size = {
    'K': 16,
    'M': 16,
    'k': 4,
    'm': 4
}
```


The strides must also be specified with a similar dict


```python
strides = {
    'K': 64,
    'M': 16,
    'k': 4,
    'm': 1
}
```

Then you can call the function
```python
visualize_strided_4d_layout(size, strides)
```
The result is stored to `result.png`
