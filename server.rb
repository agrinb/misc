require 'sinatra'
require 'pry'
require 'sinatra/reloader'
require './data_converter'

data = DataConverter.new
data = data.prep_data(data.all_rows)


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

