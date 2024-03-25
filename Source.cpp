#include <iostream>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Rus");

    std::cout << "Введите N: ";
    int N;
    std::cin >> N;
    std::cout << '\n';

    // Проверка на делимость на 2 и 5
    if (N % 2 == 0 || N % 5 == 0) {
        std::cout << "NO\n";
        return 0;
    }

    int remainder = 1;
    int count = 1;

    // Ищем число, состоящее только из единиц и кратное N
    while (remainder != 0) {
        remainder = (remainder * 10 + 1) % N;
        count++;
    }

    // Выводим число, состоящее только из единиц и кратное N
    for (int i = 0; i < count; i++) { std::cout << 1; }
    std::cout << '\n';

    return 0;
}
