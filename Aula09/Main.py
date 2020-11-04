from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

pessoaFisica = Fisica(1,"Gabriela", "Lima e Silva", "333-333","130.889.632-22", 22, 70, 1.70)
print(pessoaFisica._endereco)
print(pessoaFisica._calcula_imc())