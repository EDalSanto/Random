require 'byebug'

class Player
  attr_accessor :symbol, :name

  def initialize(symbol,name)
    @symbol = symbol
    @name = name
  end


  def select_row
    puts "#{@name} please select a row: top, middle, or bottom"
    row = gets.chomp
    if row != 'top' && row != 'middle' && row != 'bottom'
      p "There was a typo! Please try again"
      # Recursive call made to prompt user again for proper input
      row = select_row
    end
    row
  end

  def select_column
    puts "#{@name} please select a column: left, center, or right"
    column = gets.chomp
    if column != "left" && column != "center" && column != "right"
      p "There was a typo! Please try again"
      # Recursive call made to prompt user again for proper input
      column = select_column
    end
    column
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
        # Users will input english words, so we need to translate them to indexes on board
    @rows_eng_to_idx = {
      'top'=>0,
      'middle'=>1,
      'bottom'=>2
    }
    @columns_eng_to_idx = {
      'left'=>0,
      'center'=>1,
      'right'=>2
    }
  end

  def translate(row_english,column_english)
    row = @rows_eng_to_idx[row_english]
    column = @columns_eng_to_idx[column_english]
    return row,column
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
  board.spaces.transpose.each do |row| # transpose method flips rows into columns that is arrays are now grouped as columns
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
      # Get human coordinates
      row,column = player.select_row, player.select_column
      # Translate into indexes on board
      row,column = board.translate(row,column)
      if !empty_cell?(board,row,column)
        puts "Spot already filled! Skip to next player for your carelessness #{player.name} !"
      else
        board.update_board(row,column,symbol)
      end
      if won?(board,symbol) == true
        board.display_board
        p "winner, winner, chicken dinner #{player.name}!"
        # Break out of while loop 
        return
      end
      turns += 1
    end
  end
end

# Loads game
board = Board.new
player1 = Player.new("X", "John")
player2 = Player.new("O", "Bob")
play(board,player1,player2)
