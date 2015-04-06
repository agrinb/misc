require 'sinatra'
require 'pry'
require 'sinatra/reloader'
require 'csv'
require 'date'


def all_rows
  data = ''
  Dir.glob('data/*.txt') do |file|
    File.open(file) do |in_file|
      in_file.each do |line|
        #convert data to be consistent with other files
        line =  line.gsub('Male', 'M').gsub('Female', 'F')
        data << line.gsub('-', '/').gsub(' ', ',').gsub('|', ',').squeeze(' ') << "\n" #add line breaks between files
      end
    end 
  end
  data = data.squeeze("\n").squeeze(",") #remove consecutive line breaks (\n\n) 
end

def prep_data(data)
  arr = []
  CSV.parse(data) do |row|
    #adjust the colum the DOB is in
    if /([0-9]+)\/([0-9]+)\/([0-9]+)/.match(row[-1])
      row[-1], row[-2] = row[-2], row[-1]
    end
    #convert date to mm-dd-yyyy format
    row[-2] = Date.strptime(row[-2], '%m/%d/%Y').strftime('%m/%d/%Y')
    #adjust for missing middle name
    if row.length < 6
      row.insert(2, "NA")
    end
    arr << row
  end
  arr
end



data = prep_data(all_rows)


#==============================================================================
ln_index = 0
ge_index = 3
dt_index = 4

get '/' do
  @page_title = "Sorted by gender and last name"
  @data = data.sort_by.sort_by { |object| [ object[ge_index], object[ln_index] ] }
  erb :'data/data.html'
end

get '/gender_and_lastname' do
  @page_title = "Sorted by gender and last name"
  @data = data.sort_by.sort_by { |object| [ object[ge_index], object[ln_index] ] }
  erb :'data/data.html'
end

get '/birth_date' do
  @page_title = "Sorted by birth day"
  @data = data.sort_by.sort_by do |object| 
    Date.strptime(object[dt_index], '%m/%d/%Y') 
  end
  erb :'data/data.html'
end

get '/last_name' do
  @page_title = "Sorted by gender and last name"
  @data = data.sort_by.sort { |a, b| b[ln_index] <=> a[ln_index] }
  erb :'data/data.html'
end

