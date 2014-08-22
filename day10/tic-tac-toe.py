from Tkinter import *
import tkMessageBox

class MyWindow:
  def __init__(self, myParent):
    self.myContainer = Frame(myParent)
    self.myContainer.grid() 
    self.makeLayout()
    self.currentPlayer = 1 

  def makeLayout(self):
    self.currentPlayer = 1 
    self.label = Label(self.myContainer, text="Tic-Tac-Toe")
    self.label.grid(row=0, column=1, columnspan=3)

    self.whoseTurn = Label(self.myContainer, text="It is Player 1's turn")
    self.whoseTurn.grid(row=4, column=1, columnspan=3)

    self.buttons = {}
    for i in range(9):
      self.buttons[i] = Button(self.myContainer, text="", width=1, height=1, command=lambda x=i: self.tic(x) )
      self.buttons[i].grid(row=i/3+1, column=i%3+1)

  def tic(self, x):
    button = self.buttons[x]
    if (self.currentPlayer==1) and (button["text"]==""): 
      button["text"] = "X" 
      self.checkWin(x)
      self.currentPlayer = 2
      self.whoseTurn["text"] = "It is Player 2's turn"
    elif (self.currentPlayer==2) and (button["text"]==""): 
      button["text"] = "O"
      self.checkWin(x)
      self.currentPlayer = 1
      self.whoseTurn["text"] = "It is Player 1's turn"
    else: tkMessageBox.showinfo('For shame', "I have no idea who you are!")

  def checkWin(self, x):
    col = self.checkCol(x)
    row = self.checkRow(x)
    diag = self.checkDiag(x)
    if col or row or diag:
      if self.currentPlayer == 1:
        winner = "Player 1"
      else: winner = "Player 2"
      tkMessageBox.showinfo('Message', winner + " won!")
      self.makeLayout()
    if self.checkFull():
      tkMessageBox.showinfo('Message', "The cat won!")
      self.makeLayout()


  def checkCol(self, x):
    if 0<=x<=2: b = [x+3, x+6]
    elif 3<=x<=5: b = [x-3, x+3]
    else: b = [x-3, x-6]
    return self.buttons[x]["text"] ==self.buttons[b[0]]["text"]==self.buttons[b[1]]["text"]

  def checkRow(self, x):
    if x%3 == 0: b = [x+1, x+2]
    elif x%3 == 1: b = [x-1, x+1]
    else: b = [x-1, x-2]
    return self.buttons[x]["text"] ==self.buttons[b[0]]["text"]==self.buttons[b[1]]["text"]

  def checkDiag(self, x):
    if x%2 != 0: return False 
    offDiag = (self.buttons[2]["text"] == self.buttons[4]["text"] == self.buttons[6]["text"]) and (self.buttons[4]["text"] != "") 
    onDiag = (self.buttons[0]["text"] == self.buttons[4]["text"] == self.buttons[8]["text"]) and (self.buttons[4]["text"] != "") 
    return onDiag or offDiag

  def checkFull(self):
    isFull = []
    for button in self.buttons:
      isFull.append( self.buttons[button]["text"] != "" )
    full = True
    for f in isFull:
      full = full and f
    return full 

root = Tk()
root.geometry('400x300+150+40')
window = MyWindow(root)
root.title('Our Game')
root.mainloop()