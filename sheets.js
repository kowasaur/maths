/**
 * Dot product
 * @param {number[]} v1
 * @param {number[]} v2
 */
function dot(v1, v2) {
    return v1.reduce((sum, value, index) => sum + value * v2[index], 0);
}

/**
 * Get the column of a matrix
 * @param {number[][]} matrix
 * @param {number} col
 */
function mCol(matrix, col) {
    return matrix.map(row => row[col]);
}

/**
 * Multiply a matrix by a matrix
 * @param {number[][]} matrix1
 * @param {number[][]} matrix2
 */
function mMul(matrix1, matrix2) {
    return matrix1.map(row => row.map((_, x) => dot(row, mCol(matrix2, x))));
}

/**
 * Raise a matrix to a power
 * @param {number[][]} matrix
 * @param {number} power
 */
function mPow(matrix, power) {
    let new_matrix = matrix;
    while (power-- > 1) new_matrix = mMul(new_matrix, matrix);
    return new_matrix;
}

/**
 * Convert a column of survival rates into a Leslie matrix (excluding top row)
 * @param {number[][]} rates
 */
function leslieSurvival(rates) {
    rates = rates.flat();
    const matrix = [];
    for (let i = 0; i < rates.length - 1; i++) {
        const row = new Array(rates.length).fill(0);
        row[i] = rates[i];
        matrix.push(row);
    }
    return matrix;
}

console.log(
    mPow(
        [
            [5, 6, 3],
            [2, 3, 5],
            [9, 8, 7],
        ],
        4
    )
);
