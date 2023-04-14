
class ReverseStringService:

    def reverse_string(self, number: int):
        """
        Dado um número inteiro, como parâmetro, devolver o
        número inteiro com dígitos invertidos.

        :param number: int
        
        :return { reverted_number: int }:
        """
        # Cria variavel reverted_number
        reverted_number = 0

        # Verifica se o número é negativo
        if number < 0:
            # Se for negativo, inverte somente os dígitos do número sem o sinal negativo
            reverted_number = int(str(number)[1:][::-1]) * -1
        else:
            # Se for positivo, inverte todos os dígitos do número
            reverted_number = int(str(number)[::-1])
       
        # Retorna o número original e o invertido
        return number, reverted_number