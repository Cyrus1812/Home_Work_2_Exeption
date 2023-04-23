# public static void main(String[] args) throws Exception {
#    try {
#        int a = 90;
#        int b = 3;
#        System.out.println(a / b);
#        printSum(23, 234);
#        int[] abc = { 1, 2 };
#        abc[3] = 9;
#    } catch (Throwable ex) {
#        System.out.println("Что-то пошло не так...");
#    } catch (NullPointerException ex) {
#        System.out.println("Указатель не может указывать на null!");
#    } catch (IndexOutOfBoundsException ex) {
#        System.out.println("Массив выходит за пределы своего размера!");
#    }
# }
# public static void printSum(Integer a, Integer b) throws FileNotFoundException {
#    System.out.println(a + b);
# }

# В данном коде ошибка заключается в том, что блок catch (Throwable ex) 
# находится перед блоками catch для более конкретных исключений. Это приведет к тому,
#  что блок catch (Throwable ex) будет перехватывать все исключения, включая те, 
#  которые могут быть обработаны более конкретными блоками catch.


def main():
    try:
        a = 90
        b = 3
        print(a / b)
        print_sum(23, 234)
        abc = [1, 2]
        abc[3] = 9
    except TypeError:
        print("Указатель не может указывать на null!")
    except IndexError:
        print("Массив выходит за пределы своего размера!")
    except Exception:
        print("Что-то пошло не так...")

def print_sum(a, b):
    print(a + b)

if __name__ == "__main__":
    main()


# Здесь блок catch (Throwable ex) заменен на более конкретные блоки catch 
# для исключений TypeError и IndexError.