require 'byebug'

class Player
  attr_accessor :symbol, :name

  def initialize(symbol,name)
    @symbol = symbol
    @name = name
  end

  def select_row(board)
    puts "#{@name} please select a row: top, middle, or bottom"
    row = gets.chomp
    if !board.valid_inputs_row.include?(row)
      p "There was a typo! Please try again"
      # Recursive call made to prompt user again for proper input
      row = select_row(board)
    end
    row
  end

  def select_column(board)
    puts "#{@name} please select a column: left, center, or right"
    column = gets.chomp
    if !board.valid_inputs_col.include?(column)
      p "There was a typo! Please try again"
      # Recursive call made to prompt user again for proper input
      column = select_column(board)
    end
    column
  end

end

class Board
  attr_accessor :spaces, :players
  attr_reader :valid_inputs_col, :valid_inputs_row

  def initialize
    # Create spaces on board
    @spaces = [
      ["-","-","-"],
      ["-","-","-"],
      ["-","-","-"]
    ]
    # Create two players needed to play game, as well as array of players
    @player1 = Player.new("X", "John")
    @player2 = Player.new("O", "Bob")
    @players = [@player1, @player2]
    # Users will input english words, so we need to translate them to indexes on board
    @valid_inputs_row = ['top', 'middle', 'bottom']
    @valid_inputs_col = ['left', 'center', 'right']
    # Hash Constructor accepts array of key values pairs
    # Map over each possible input with index that will be the val
    @rows_eng_to_idx = Hash[@valid_inputs_row.each_with_index.map { |input, index| [input, index]} ]
    @columns_eng_to_idx = Hash[@valid_inputs_col.each_with_index.map { |input, index| [input, index]} ]

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

def play(board)
  turns = 0
  while turns < 9
    board.players.each do |player|
      symbol = player.symbol
      board.display_board
      # Get human coordinates
      row,column = player.select_row(board), player.select_column(board)
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
play(board)
