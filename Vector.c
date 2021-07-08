#include <stdio.h>
#include <math.h>

typedef struct Vector {
    double i;
    double j;
} Vector;

double v_magnitude(Vector v) {
    return sqrt(v.i * v.i + v.j * v.j);
}

Vector v_unitVector(Vector v) {
    double mag = v_magnitude(v);
    Vector u = {v.i / mag, v.j / mag};
    return u;
}

double v_dotProduct(Vector v1, Vector v2) {
    return v1.i * v2.i + v1.j * v2.j;
}

double v_scalarResolute(Vector v1, Vector v2) {
    return v_dotProduct(v1, v_unitVector(v2));
}

void inputNum(char prompt[], double *var) {
    printf("%s", prompt);
    scanf("%lf", var);
}

int main() {
    double ai, aj, bi, bj;
    inputNum("Horizontal component of vector a: ", &ai);
    inputNum("Vertical component of vector a: ", &aj);
    inputNum("Horizontal component of vector b: ", &bi);
    inputNum("Vertical component of vector b: ", &bj);

    Vector a = {ai, aj};
    Vector b = {bi, bj};

    printf("\nThe scalar resolute of a on b is %g", v_scalarResolute(a, b));

    return 0;
}
