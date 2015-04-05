require 'sinatra'
require 'pry'
require 'sinatra/reloader'
require 'csv'
require 'date'


data = ''
Dir.glob('data/*.txt') do |file|
  File.open(file) do |in_file|
    in_file.each do |line|
      line =  line.gsub('Male', 'M').gsub('Female', 'F')
      data << line.gsub('-', '/').gsub(',', ' ').gsub('|', ' ').squeeze(' ') << "\n"
    end
  end 
end
data = data.squeeze("\n")

arr = []
CSV.parse(data) do |row|
  row = row[0].split(" ")
  if /([0-9]+)\/([0-9]+)\/([0-9]+)/.match(row[-1])
    row[-1], row[-2] = row[-2], row[-1]
  end
  row[-2] = Date.strptime(row[-2], '%m/%d/%Y').strftime('%m/%d/%Y')
  if row.length < 6
    row.insert(2, nil)
  end
  arr << row
end 

data = arr


#==============================================================================
ln_index = 0
ge_index = 3
dt_index = 4

get '/genres_and_lastname' do
  @data = data.sort_by.sort_by { |object| [ object[ge_index], object[ln_index] ] }
  erb :'data/data.html'
end

get '/birth_date' do
  #binding.pry
  @data = data.sort_by.sort_by do |object| 
    Date.strptime(object[dt_index], '%m/%d/%Y') 
  end
  erb :'data/data.html'
end

get '/lastname' do
  @data = data.sort_by.sort { |a, b| b[ln_index] <=> a[ln_index] }
  erb :'data/data.html'
end

