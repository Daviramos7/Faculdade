1. Boleanos
2. Caractere
3. Números
4. Temporais

## 1. Boleanos
Por padrão ele é inicializado como nulo, e pode receber tanto 1 ou 0
BIT

## 2. Caracteres
Tamanho fixo - char // Permite inserir até uma quantidade fixa de caracteres e sempre ocupa todo o espaço reservado 10/50
Tamanhos variáveis - varchar ou nvarchar // Permite inserir até uma quantidade que for definida, porem só usa o espaço que for preenchido 10/50

## 3. Numeros
### Valores Exatos

1. TINYINT - não tem parte valor fracionados (ex: 1.43, 24.23) somente 1,123123,324234,313123 etc...
2. SMALLINT - mesma coisa porem limite maior
3. INT - mesma coisa porem limite maior
4. BIGINT - mesma coisa porem limite maior
5. NUMERIC ou DECIMAL - valores exatos, porem permite ter parte fracionadosm, que também pode ser especificado a precisão e escala (escala é o número de digitos na parte fracional) ex: NUMERIC (5,2) 113,44

### Valores Aproximados

1. REAL - Tem precisão aproximada de até 15 digitos
2. FLOAT - mesmo conceito de REAL

## 4. Temporais
DATE - armazena data no formato aaaa/mm/dd
DATETIME - armazena data no formato aaaa/mm/dd:hh:mm:ss
DATATIME2 - data e hora com adição de milissegundos no formato aaaa/mm/dd:hh:mm:sssssss
SMALLDATETIME - data e hora nos respeitando o limite entre 1900 até 2079
TIME - horas, minutos, segundos e milissegundos respeitando o limite total
DATETIMEOFFSET - permite armazenar informações de data e horas incluindo o fuso horário