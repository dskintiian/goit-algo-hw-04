# Домашнє завдання до теми “Алгоритми сортування”

Python має дві вбудовані функції сортування: `sorted` і `sort`. Функції сортування Python використовують Timsort — гібридний алгоритм сортування, що поєднує в собі сортування злиттям і сортування вставками.

Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання. Аналіз повинен бути підтверджений емпіричними даними, отриманими шляхом тестування алгоритмів на різних наборах даних. Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах. Для заміру часу виконання алгоритмів використовуйте модуль timeit.

Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, і саме з цієї причини програмісти, в більшості випадків, використовують вбудовані в Python алгоритми, а не кодують самі. Зробіть висновки.

### Необов'язкове завдання

Дано `k` відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. При виконанні завдання можете опиратися на алгоритм сортування злиттям з конспекту. Реалізуйте функцію `merge_k_lists` , яка приймає на вхід список відсортованих списків та повертає відсортований список.

Приклад очікуваного результату:
```
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
```

Виведення:
```
Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
```

## Результат аналізу алгоритмів сортування

| Розмір семплу | Алгоритм       | Час виконання         |
|---------------|----------------|-----------------------|
| 10            | sort           | 0.0005632080137729645 |
| 10            | sorted         | 0.001200250000692904  |
| 10            | insertion_sort | 0.00643229199340567   |
| 10            | merge_sort     | 0.04661095899064094   |
| 100           | sort           | 0.002451209002174437  |
| 100           | sorted         | 0.004530125006567687  |
| 100           | insertion_sort | 0.061100499995518476  |
| 100           | merge_sort     | 0.7027464169659652    |
| 1000          | sort           | 0.02036137494724244   |
| 1000          | sorted         | 0.031084999965969473  |
| 1000          | insertion_sort | 0.7117860830039717    |
| 1000          | merge_sort     | 9.151106791046914     |
| 10000         | sort           | 0.2555592500139028    |
| 10000         | sorted         | 0.5159328749869019    |
| 10000         | insertion_sort | 7.474804833997041     |
| 10000         | merge_sort     | 116.67421150003793    |
| 100000        | sort           | 3.0900720420177095    |
| 100000        | sorted         | 5.381920458981767     |
| 100000        | insertion_sort | 81.00878475001082     |
| 100000        | merge_sort     | 1467.5050630419864    |

Як видно з таблиці, найоптимальніший алгоритм сортування - Timsort і метод sort().    