from Funcionarios import Funcionario

flavio = Funcionario('Flávio', 'flavionuneslopes@hotmail.com')

flavio.cadastro_hora('Jan', 300)
flavio.cadastro_hora('Fev', 200)
flavio.cadastro_salario_hora('Jan', 30)
flavio.cadastro_salario_hora('Fev', 30)
print(flavio)
print(f"Salário de Jan: {flavio.calcula_salario('Jan')}")
print(f"Salário de Fev: {flavio.calcula_salario('Fev')}")
