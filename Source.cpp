#include <iostream>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Rus");

    std::cout << "������� N: ";
    int N;
    std::cin >> N;
    std::cout << '\n';

    // �������� �� ��������� �� 2 � 5
    if (N % 2 == 0 || N % 5 == 0) {
        std::cout << "NO\n";
        return 0;
    }

    int remainder = 1;
    int count = 1;

    // ���� �����, ��������� ������ �� ������ � ������� N
    while (remainder != 0) {
        remainder = (remainder * 10 + 1) % N;
        count++;
    }

    // ������� �����, ��������� ������ �� ������ � ������� N
    for (int i = 0; i < count; i++) { std::cout << 1; }
    std::cout << '\n';

    return 0;
}
