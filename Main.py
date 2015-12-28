import Piece
import Machine
import Entrepot
import Message

# launch all of our queued processes
def main():
    print("----- DEBUT SIMULATION ENTREPOT -----")

    # Pièces
    Piece.processusPieces()

    # Machine mA
    Machine.processusMachine("mA",["pA", "pB"],["mB"])

    # Machine mB
    Machine.processusMachine("mB",["pB", "pC"],["mA"])

    # Entrepôt
    # Entrepot.processusEntrepot()

    print("------ FIN SIMULATION ENTREPOT ------")

main()