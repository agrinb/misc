require 'csv'
require 'pry'
require 'date'


data = ''
Dir.glob('data/*.txt') do |file|
  File.open(file) do |in_file|
    #File.open("combined_output.csv", 'a') do |out_file| #the 'w' opens the file for writing
    in_file.each do |line| 
      data << line.gsub(',', ' ').gsub('|', ' ').squeeze(' ') << "\n"
    end
  end 
  # CSV.foreach(file, 'r+') do |in_file|    
  #   CSV.open("data/combined_output.csv", 'a', {:col_sep => "\t"}) do |out_file| #the 'w' opens the file for writing
  #       out_file << in_file.map { |el| el.gsub('|', ' ').gsub(',', ' ').squeeze(' ') }
  #   end 
  # end
end
data = data.squeeze("\n")


CSV.open("data/combined_output.csv", 'a', {:col_sep => ","}) do |csv|
  CSV.parse(data) do |row|
    csv << row[0].split(" ")
  end 
end




