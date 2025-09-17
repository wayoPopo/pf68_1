#include <iostream>
#include <vector>
#include <random>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <string>
#include <sstream>
#include <cmath>

using Matrix = std::vector<std::vector<float>>;

void printMatrix(const Matrix& matrix, const std::string& title) {
    std::cout << "--- " << title << " ---\n";
    for (const auto& row : matrix) {
        for (float val : row) {
            std::cout << std::fixed << std::setprecision(2) << std::setw(8) << val;
        }
        std::cout << std::endl;
    }
    std::cout << "------------------------\n";
}

float calculateDeterminant(const Matrix& coeffs) {
    float det = 0;
    det += coeffs[0][0] * (coeffs[1][1] * coeffs[2][2] - coeffs[1][2] * coeffs[2][1]);
    det -= coeffs[0][1] * (coeffs[1][0] * coeffs[2][2] - coeffs[1][2] * coeffs[2][0]);
    det += coeffs[0][2] * (coeffs[1][0] * coeffs[2][1] - coeffs[1][1] * coeffs[2][0]);
    return det;
}

Matrix generateSolvableSystem(int& sol_x, int& sol_y, int& sol_z) {
    std::mt19937 gen(time(0));
    std::uniform_int_distribution<> sol_dist(-5, 5);
    std::uniform_int_distribution<> coeff_dist(-10, 10);
    sol_y = sol_dist(gen);
    sol_z = sol_dist(gen);

    Matrix augmentedMatrix(3, std::vector<float>(4));
    Matrix coefficients(3, std::vector<float>(3));
    float determinant = 0;
    std::stringstream equationsStream;

    do {
        equationsStream.str("");
        //std::cout << "random coefficeint...\n";

        for (int i = 0; i < 3; ++i) {
            // 2.1 สุ่มสัมประสิทธิ์ a, b, c
            int a = coeff_dist(gen);
            int b = coeff_dist(gen);
            int c = coeff_dist(gen);

            int d = (a * sol_x) + (b * sol_y) + (c * sol_z);

            coefficients[i][0] = a;
            coefficients[i][1] = b;
            coefficients[i][2] = c;
            augmentedMatrix[i] = { (float)a, (float)b, (float)c, (float)d };

            equationsStream << a << "x + " << b << "y + " << c << "z = " << d << "\n";
        }
        determinant = calculateDeterminant(coefficients);
        //std::cout << "test Determinant: " << determinant << std::endl;

    } while (std::abs(determinant) < 1e-6);

    //std::cout << "\nFound solution!\n";

    // 4. save testcase.txt
    std::ofstream testcaseFile("../testcases/testcase.txt");
    testcaseFile << equationsStream.rdbuf();
    testcaseFile.close();
    std::cout << " save test data -> save testcase.txt \n";

    return augmentedMatrix;
}

//  Gauss-Jordan Elimination
void performGaussJordan(Matrix& matrix) {
    const int ROWS = matrix.size();
    if (ROWS == 0) return;
    const int COLS = matrix[0].size();

    int pivot_row = 0;
    for (int j = 0; j < COLS - 1 && pivot_row < ROWS; ++j) {
        // partial pivot
        int max_row = pivot_row;
        for (int i = pivot_row + 1; i < ROWS; ++i) {
            if (std::abs(matrix[i][j]) > std::abs(matrix[max_row][j])) {
                max_row = i;
            }
        }
        // swap row
        std::swap(matrix[pivot_row], matrix[max_row]);

        // find pivot 1
        float pivot_val = matrix[pivot_row][j];
        if (std::abs(pivot_val) < 1e-9) continue; //all 0

        for (int k = j; k < COLS; ++k) {
            matrix[pivot_row][k] /= pivot_val;
        }

        // eliminate 0
        for (int i = 0; i < ROWS; ++i) {
            if (i != pivot_row) {
                float factor = matrix[i][j];
                for (int k = j; k < COLS; ++k) {
                    matrix[i][k] -= factor * matrix[pivot_row][k];
                }
            }
        }
        pivot_row++;
    }
}


// --- Main Program ---
int main() {
    int x, y, z;
    Matrix system = generateSolvableSystem(x, y, z);
    
    // 5. save augmented matrix to ../testcases/solution0.txt
    std::ofstream solution0File("../testcases/solution0.txt");
    std::cout<<"save augmented -> solution0.txt \n";
    for(const auto& row : system) {
        solution0File << row[0] << " " << row[1] << " " << row[2] << " " << row[3] << "\n";
    }
    solution0File.close();
    //std::cout << " -> บันทึก Augmented Matrix ลงใน solution0.txt เรียบร้อย\n";

    // 5. บันทึกคำตอบ x,y,z ลงไฟล์ solution1.txt
    std::ofstream solution1File("../testcases/solution1.txt");
    std::cout<<"save solution --> solution1.txt\n";
    solution1File << x << "\n";
    solution1File << y << "\n";
    solution1File << z << "\n";
    solution1File.close();
    //std::cout << " -> บันทึกคำตอบที่สุ่มได้ลงใน solution1.txt เรียบร้อย\n\n";

    //printMatrix(system, "Augmented Matrix เริ่มต้น");

    // แก้สมการด้วย Gauss-Jordan
    performGaussJordan(system);

    //printMatrix(system, "Matrix หลังทำ Gauss-Jordan (Reduced Row Echelon Form)");
    
    // แสดงผลคำตอบ
    //std::cout << "คำตอบจากการคำนวณ:\n";
//    std::cout << std::fixed << std::setprecision(0);
//    std::cout << "x = " << system[0][3] << std::endl;
//    std::cout << "y = " << system[1][3] << std::endl;
//    std::cout << "z = " << system[2][3] << std::endl;
    
    return 0;
}