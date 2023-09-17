#include <iostream>
#include <vector>

int main() {
    int t;
    std::cin >> t;

    while (t--) {
        int n;
        std::cin >> n;
        std::vector<int> perms(n);

        for (int i = 0; i < n; i++) {
            std::cin >> perms[i];
        }

        int node = 0;
        int components = 0;
        for (int i = 0; i < n; i++) {
            node = std::max(node, perms[i]);
            if (node <= i + 1) {
                components++;
            }
        }

        std::cout << components << std::endl;
    }

    return 0;
}
