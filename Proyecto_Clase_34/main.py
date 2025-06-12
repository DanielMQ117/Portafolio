import pickle


class Student():
    """Clase que representa a un estudiante y sus asignaturas."""

    def __init__(self, name, carnet):
        # Atributos de instancia
        self.name = name
        self.carnet = carnet
        self.subjects = []  # Lista de diccionarios para las asignaturas

    def add_subject(self, subject_name, credits, qualification=0.0):
        """Agrega una asignatura al estudiante."""
        subject = {
            'name': subject_name,
            'estate': 'Aprobada' if qualification >= 60 else 'Reprobada',
            'credits': credits,
            'qualification': qualification
        }
        self.subjects.append(subject)

    def show_subjects(self, estate=False, credits=False, qualification=False):
        """Devuelve la lista de asignaturas del estudiante."""
        for subject in self.subjects:
            print(f"\tAsignatura: {subject['name']}; ", end='')
            (print(f"Créditos: {subject['credits']}; ", end='')
             ) if credits == 1 else None
            (print(f"Calificación: {subject['qualification']}; ", end='')
             ) if qualification == 1 else None
            (print(f"Estado: {subject['estate']}")
             ) if estate == 1 else None

        print("")


class App():
    """Clase principal de la aplicación que gestiona el menú y las opciones del programa."""
    # Atributo de clase
    students = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def style_print(function):
        """Decorador para aplicar un estilo a la funcion 'print()'."""
        def wrapper(*args, **kwargs):
            args = list(args)
            width = len(args[1]) + (10 * 2)
            args[1] = "|" + str(args[1]).center(width, ' ') + "|"
            print("\n" + "+" + "-" * width + "+")
            print("|" + " " * width + "|")
            function(*tuple(args), **kwargs)
            print("|" + " " * width + "|")
            print("+" + "-" * width + "+" + "\n")
        return wrapper

    def add_student(self):
        """Permite ingresar un nuevo estudiante y sus asignaturas."""
        print("***** INGRESAR DATOS DEL ESTUDIANTE *****")
        name = input("Nombre: ").strip(' ')
        carnet = input("Número de carnet: ").strip(' ')
        student = Student(name, carnet)
        self.students.append(student)

        print("")
        option = input("Desea agregar asignaturas? (s/n): ").lower().strip(' ')
        while option == 's':
            subject_name = input("Nombre de la asignatura: ").strip(' ')
            creditos = int(input("Número de créditos: ").strip(' '))
            qualification = float(input("Calificación obtenida: ").strip(' '))
            student.add_subject(
                subject_name, creditos, qualification=qualification)
            print("Asignatura agregada exitosamente.")

            print("")
            option = input(
                "Desea agregar otra asignatura? (s/n): ").lower().strip(' ')
            if option != 's':
                break

    def show_student(self):
        """Muestra todos los estudiantes y sus asignaturas."""
        print("***** LISTADO DE ESTUDIANTES *****")
        if not self.students:
            self._message("No hay estudiantes registrados!")
            return

        print("")
        for student in self.students:
            print(
                f" -> Carnet: {student.carnet}; Nombre: {student.name}; ", end='')
            if student.subjects:
                student.show_subjects()
            else:
                self._message("No tiene asignaturas registradas.")

        print("\n - Total de estudiantes: ", len(self.students), end='\n\n')

    def find_student(self):
        """Busca un estudiante por su número de carnet."""
        print("***** BUSCAR ESTUDIANTE *****")
        print("")
        carnet = input("Ingrese el número de carnet: ").strip(' ')

        for student in self.students:
            if student.carnet == carnet:
                self._message(f"Estudiante encontrado: {student.name}")
                student.show_subjects(
                    estate=True, credits=True, qualification=True)
                return

        self._message("Estudiante no encontrado!")

    def save_data(self):
        """Guarda los datos de los estudiantes en un archivo."""
        print("***** GUARDAR DATOS *****")
        with open('students_data.pkl', 'wb') as file:
            pickle.dump(self.students, file)
        self._message("Datos guardados exitosamente!")

    def load_data(self):
        """Carga los datos de los estudiantes desde un archivo."""
        print("***** CARGAR DATOS *****")
        try:
            with open('students_data.pkl', 'rb') as file:
                self.students = pickle.load(file)
            self._message("Datos cargados exitosamente!")
        except FileNotFoundError:
            self._message("No se encontraron datos guardados!")
        except Exception as e:
            self._message(f" >> Error al cargar los datos: {e}")

    @style_print
    def _message(self, string: str):
        """Imprime un mensaje con un estilo específico."""
        print(string)

    def options(self):
        print("***** MENÚ DE OPCIONES *****")
        print("\t1. Ingresar un estudiante")
        print("\t2. Ver todos los estudiantes")
        print("\t3. Buscar un estudiante")
        print("\t4. Guardar datos")
        print("\t5. Cargar datos")
        print("\t6. Salir")
        return int(input("-> Elija su opción: ").strip(' '))

    def menu(self):
        while True:
            match self.options():
                case 1:
                    self.add_student()
                case 2:
                    self.show_student()
                case 3:
                    self.find_student()
                case 4:
                    self.save_data()
                case 5:
                    self.load_data()
                case 6:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    application = App()
    application.menu()
