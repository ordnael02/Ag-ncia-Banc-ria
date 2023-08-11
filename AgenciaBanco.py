package OAC;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class ContaBancaria {
    private int numeroConta;
    private String nomeTitular;
    private double saldo;

    public ContaBancaria(int numeroConta, String nomeTitular, double saldoInicial) {
        this.numeroConta = numeroConta;
        this.nomeTitular = nomeTitular;
        this.saldo = saldoInicial;
    }

    public int getNumeroConta() {
        return numeroConta;
    }

    public String getNomeTitular() {
        return nomeTitular;
    }

    public double getSaldo() {
        return saldo;
    }

    public void depositar(double valor) {
        saldo += valor;
        System.out.println("Depósito de R$" + valor + " realizado. Novo saldo: R$" + saldo);
    }

    public void sacar(double valor) {
        if (valor <= saldo) {
            saldo -= valor;
            System.out.println("Saque de R$" + valor + " realizado. Novo saldo: R$" + saldo);
        } else {
            System.out.println("Saldo insuficiente para saque.");
        }
    }
}

class AgenciaBancaria {
    private int numeroAgencia;
    private List<ContaBancaria> contas;

    public AgenciaBancaria(int numeroAgencia) {
        this.numeroAgencia = numeroAgencia;
        this.contas = new ArrayList<>();
    }

    public void adicionarConta(ContaBancaria conta) {
        contas.add(conta);
        System.out.println("Conta " + conta.getNumeroConta() + " adicionada à agência " + numeroAgencia);
    }

    public void realizarDeposito(int numeroConta, double valor) {
        for (ContaBancaria conta : contas) {
            if (conta.getNumeroConta() == numeroConta) {
                conta.depositar(valor);
                break;
            }
        }
    }

    public void realizarSaque(int numeroConta, double valor) {
        for (ContaBancaria conta : contas) {
            if (conta.getNumeroConta() == numeroConta) {
                conta.sacar(valor);
                break;
            }
        }
    }
}

public class TesteAgenciaBancaria {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o número da agência: ");
        int numeroAgencia = scanner.nextInt();
        AgenciaBancaria agencia = new AgenciaBancaria(numeroAgencia);

        System.out.print("Quantas contas você deseja criar? ");
        int numContas = scanner.nextInt();

        for (int i = 0; i < numContas; i++) {
            System.out.print("Digite o número da conta: ");
            int numeroConta = scanner.nextInt();

            System.out.print("Digite o nome do titular: ");
            scanner.nextLine(); // Limpar o buffer
            String nomeTitular = scanner.nextLine();

            System.out.print("Digite o saldo inicial: ");
            double saldoInicial = scanner.nextDouble();

            ContaBancaria conta = new ContaBancaria(numeroConta, nomeTitular, saldoInicial);
            agencia.adicionarConta(conta);
        }

        while (true) {
            System.out.println("Escolha uma opção:");
            System.out.println("1 - Realizar depósito");
            System.out.println("2 - Realizar saque");
            System.out.println("3 - Sair");
            int opcao = scanner.nextInt();

            if (opcao == 1) {
                System.out.print("Digite o número da conta: ");
                int numeroConta = scanner.nextInt();

                System.out.print("Digite o valor do depósito: ");
                double valor = scanner.nextDouble();

                agencia.realizarDeposito(numeroConta, valor);
            } else if (opcao == 2) {
                System.out.print("Digite o número da conta: ");
                int numeroConta = scanner.nextInt();

                System.out.print("Digite o valor do saque: ");
                double valor = scanner.nextDouble();

                agencia.realizarSaque(numeroConta, valor);
            } else if (opcao == 3) {
                System.out.println("Saindo do programa...");
                break;
            } else {
                System.out.println("Opção inválida. Escolha novamente.");
            }
        }

        scanner.close();
    }
}
