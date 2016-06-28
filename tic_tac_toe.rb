class Player
  attr_accessor :symbol

  def initialize(symbol)
    @symbol = symbol
  end

end

class Board
  attr_accessor :spaces

  def initialize
    @spaces = [
      ["-","-","-"],
      ["-","-","-"],
      ["-","-","-"]
    ]
  end

  def get_cell(row,column)
    @spaces[row][column]
  end

  def update_board(row,column,symbol)
    @spaces[row][column] = symbol
  end

  def display_board
    @spaces.each do |row|
      print "|"
      row.each { |cell| print "  #{cell}  |" }
      puts "\n-------------------"
    end
  end

  def diagonals
    [
      [get_cell(0, 0), get_cell(1, 1), get_cell(2, 2)],
      [get_cell(0, 2), get_cell(1, 1), get_cell(2, 0)]
    ]
  end

end

def select_location(player)
  puts "#{player} please select row: 0,1,or 2"
  row = gets.chomp.to_i
  puts "And please select a column: 0,1,or 2 "
  column = gets.chomp.to_i
  return row,column
end

# winning_positions


def won?(board,symbol)
  # What are the winning states?
  # Same symbol for entire row
  board.spaces.each do |row|
    if row.all? { |cell| cell == symbol }
      return true
    end
  end
  # Same symbol for entire column
  board.spaces.transpose.each do |row|
    if row.all? { |cell| cell == symbol }
      return true
    end
  end
  board.diagonals.each do |row|
    if row.all? { |cell| cell == symbol }
      return true
    end
  end
  return false
end

def empty_cell?(board,row,column)
  return board.get_cell(row,column) == "-"
end

def play(board,*players)
  turns = 0
  while turns < 9
    players.each do |player|
      symbol = player.symbol
      board.display_board
      row,column = select_location(player)
      if row > 2 || row < 0 || column < 0 || column > 2
        puts "your row and columns must be between 0 and 2. Please try again #{player} !"
      elsif !empty_cell?(board,row,column)
        puts "spot already filled! Skip to next player for your carelessness #{player} !"
      else
        board.update_board(row,column,symbol)
      end
      turns += 1
      if won?(board,symbol) == true
        board.display_board
        return "winner, winner, chicken dinner!"
      end
    end
  end
end

# Loads game
board = Board.new
player1 = Player.new("X")
player2 = Player.new("O")
play(board,player1,player2)
