class Base:
    def __init__(self, pNome, pIdade, pCpf, pTelefoneResidencia, pTelefoneCelular, pEndereco):
        self.FNome = pNome
        self.FIdade = pIdade
        self.FCpf = pCpf
        self.FTelefoneResidencia = pTelefoneResidencia
        self.FTelefoneCelular = pTelefoneCelular
        self.FEndereco = pEndereco

class Pessoa(Base):
    def __init__(self, pNome, pIdade, pCpf, pTelefoneResidencia, pTelefoneCelular, pEndereco):
        super().__init__(pNome, pIdade, pCpf, pTelefoneResidencia, pTelefoneCelular, pEndereco)

class Professor(Base):
    def __init__(self, pNome, pIdade, pCpf, pTelefoneResidencia, pTelefoneCelular, pEndereco, pHorasAula, pValorHora):
        super().__init__(pNome, pIdade, pCpf, pTelefoneResidencia, pTelefoneCelular, pEndereco)
        self.FHorasAula = pHorasAula
        self.FTotalSalario = self.CalcularSalario(pValorHora) 

    def CalcularSalario(self, pValorHora):
        vTotalSalario = self.FHorasAula * pValorHora 
        vTotalSalario = "{:,.2f}".format(vTotalSalario)
        return vTotalSalario

class TecnicoAdministrativo(Base):
    def __init__(self, pNome, pIdade, pCpf, pTelefoneResidencia, pTelefoneCelular, pEndereco, pSalario):
        super().__init__(pNome, pIdade, pCpf, pTelefoneResidencia, pTelefoneCelular, pEndereco)
        self.FSalario = "{:,.2f}".format(pSalario)

class Curso:
    def __init__(self, pNome, pAreaAtuacao, pDataInicio, pVagas):
        self.FNome = pNome
        self.FAreaAtuacao = pAreaAtuacao
        self.FDataInicio = pDataInicio
        self.FVagas = pVagas

class UCDB:
    def __init__(self, pEndereco, pAnoFundacao):
        self.FEndereco = pEndereco
        self.FAnoFundacao = pAnoFundacao
        self.FCursos = []
        self.FProfessores = []
        self.FTecnicoAdm = []

    def CadastrarTecnico(self, pTecnicoAdm):
        self.FTecnicoAdm.append(pTecnicoAdm)

    def CadastrarCurso(self, pCurso):
        self.FCursos.append(pCurso)

    def CadastrarProfessor(self, pProfessor):
        self.FProfessores.append(pProfessor)

    def RetornarTodosProfessores(self):
        for vProfessor in self.FProfessores:
            print(f"Nome: {vProfessor.FNome}\nSalário: {vProfessor.FTotalSalario}\n")

    def RetornarTodosCursos(self):
        for vCurso in self.FCursos:
            print(f"Nome: {vCurso.FNome}\nÁrea: {vCurso.FAreaAtuacao}\n")

    def RetornarTodosTecnicosAdm(self):
        for vTecnicoAdm in self.FTecnicoAdm:
            print(f"Nome: {vTecnicoAdm.FNome}\nSalario: {vTecnicoAdm.FSalario}\n")

    def RetornarCursoPorArea(self, pArea):
        for vCurso in self.FCursos:
            if vCurso.FAreaAtuacao != pArea:
                continue
            
            print(f"Nome: {vCurso.FNome}\nÁrea: {vCurso.FAreaAtuacao}\n")

    def RetornarProfessoresPorSalario(self, pSalario):
        vSalario = "{:,.2f}".format(pSalario)

        for vProfessor in self.FProfessores:
            if vProfessor.FTotalSalario >= vSalario:
                print(f"Nome: {vProfessor.FNome}\nSalário: {vProfessor.FTotalSalario}\n")

    def RetornarProfessoresPorIdade(self, pIdade):
        for vProfessor in self.FProfessores:
            if vProfessor.FIdade >= pIdade:
                print(f"Nome: {vProfessor.FNome}\nIdade: {vProfessor.FIdade}\n")

    def RetornarGastoMensalProfessor(self):
        vTotalGasto = sum(float(vProfessor.FTotalSalario.replace(',', '')) for vProfessor in self.FProfessores)
        vTotalGasto = "{:,.2f}".format(vTotalGasto)
        print(f"Gasto mensal com professores: R${vTotalGasto}\n")

    def RetornarGastoMensalFuncionario(self):
        vTotalGasto = sum(float(vTecnicoAdm.FSalario.replace(',', '')) for vTecnicoAdm in self.FTecnicoAdm)
        print(f"Gasto mensal com funcionario: {vTotalGasto}\n")

    def RetornarProfessorMaiorSalario(self):
        vSalarioMaximo = max(self.FProfessores, key = lambda vProfessor: vProfessor.FTotalSalario)
        print(f"Professor com maior salário: {vSalarioMaximo.FNome}\nSalário: R${vSalarioMaximo.FTotalSalario}\n")

    def RetornarProfessorMaiorIdade(self):
        vIdadeMaxima = max(self.FProfessores, key = lambda vProfessor: vProfessor.FIdade)
        print(f"Professor mais velho: {vIdadeMaxima.FNome}\nIdade: {vIdadeMaxima.FIdade}\n")

    def RetornarCursoMaisAntigo(self):
        vCursoAntigo = min(self.FCursos, key = lambda vCurso: vCurso.FDataInicio)
        print(f"Curso mais antigo: {vCursoAntigo.FNome}\nData de início: {vCursoAntigo.FDataInicio}\n")

def AdicionarProfessores(pUCDB):
    vProfessor1 = Professor("João", 40, "123.456.789-00", "111-2222", "9999-8888", "Rua XPTO, 456", 40, 500)
    vProfessor2 = Professor("Maria", 35, "987.654.321-00", "333-4444", "7777-6666", "Rua ZZZ, 789", 30, 1200)
    pUCDB.CadastrarProfessor(vProfessor1)
    pUCDB.CadastrarProfessor(vProfessor2)

def AdicionarCursos(pUCDB):
    vCurso1 = Curso("Engenharia Civil", "Exatas", "01/03/2000", 200)
    vCurso2 = Curso("Medicina", "Saúde", "15/08/1995", 400)
    vCurso3 = Curso("Letras", "Humanas", "15/08/1998", 100)
    pUCDB.CadastrarCurso(vCurso1)
    pUCDB.CadastrarCurso(vCurso2)
    pUCDB.CadastrarCurso(vCurso3)

def ExibirMenu():
    print("Menu:")
    print("1. Consultar Cursos")
    print("2. Consultar Professores")
    print("3. Consultar técnicos administrativos")
    print("4. Consultar cursos por área")
    print("5. Consultar professores por salário")
    print("6. Consultar professores por idade")
    print("7. Calcular gastos mensais com professores")
    print("8. Calcular gastos mensais com técnicos administrativos ")
    print("9. Encontrar professor com maior salário")
    print("10. Encontrar professor mais idoso")
    print("11. Encontrar curso mais antigo")
    print("0. Sair")

def PopularClasse(pUCDB):
    AdicionarProfessores(pUCDB)
    AdicionarCursos(pUCDB)

    vTecnicoAdm = TecnicoAdministrativo("Mariana", 55, "787.624.121-90", "366-1236", "8888-1111", "Rua ZZZ, 789", 3000)
    pUCDB.CadastrarTecnico(vTecnicoAdm)

def RodarAplicacao():
    vUCDB = UCDB("Avenida Tamandaré, 5000", 1990)
    PopularClasse(vUCDB)

    while True:
        ExibirMenu()
        vEscolha = input("vEscolha uma opção: ")

        if vEscolha == "1":
            print("\nCursos:")
            vUCDB.RetornarTodosCursos()
            
        elif vEscolha == "2":
            print("\nDocentes:\n")
            vUCDB.RetornarTodosProfessores()

        elif vEscolha == "3":
              print("\nFuncionarios:\n")
              vUCDB.RetornarTodosTecnicosAdm()

        elif vEscolha == "4":
            vTipo = input("Digite a área a ser pesquisada: ")
            print("\nCurso de área especificada:", vTipo)
            vUCDB.RetornarCursoPorArea(vTipo)

        elif vEscolha == "5":
            vSalarioMinimo = float(input("Digite o salário mínimo: "))
            vUCDB.RetornarProfessoresPorSalario(vSalarioMinimo)

        elif vEscolha == "6":
            vIdadeMinima = int(input("Digite a idade mínima: "))
            vUCDB.RetornarProfessoresPorIdade(vIdadeMinima)

        elif vEscolha == "7":
            vUCDB.RetornarGastoMensalProfessor()

        elif vEscolha == "8":
            vUCDB.RetornarGastoMensalFuncionario()

        elif vEscolha == "9":
            vUCDB.RetornarProfessorMaiorSalario()

        elif vEscolha == "10":
            vUCDB.RetornarProfessorMaiorIdade()

        elif vEscolha == "11":
            vUCDB.RetornarCursoMaisAntigo()

        elif vEscolha == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. vEscolha uma opção válida.")

RodarAplicacao()