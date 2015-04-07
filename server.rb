require 'sinatra'
require 'pry'
require 'sinatra/reloader'
require_relative "data_converter"

dc = DataConverter.new
data = dc.prep_data(dc.all_rows)


#==============================================================================
ln_index = 0
ge_index = 3
dt_index = 4

get '/' do
  @page_title = "Sorted by gender and last name"
  @data = data.sort_by.sort_by { |object| [ object[ge_index], object[ln_index] ] }
  erb :'data/index.html'
end

get '/gender_and_lastname' do
  @page_title = "Sorted by gender and last name"
  @data = data.sort_by.sort_by { |object| [ object[ge_index], object[ln_index] ] }
  erb :'data/index.html'
end

get '/birthday' do
  @page_title = "Sorted by birth day"
  @data = data.sort_by.sort_by do |object| 
    Date.strptime(object[dt_index], '%m/%d/%Y') 
  end
  erb :'data/index.html'
end

get '/lastname' do
  @page_title = "Sorted by gender and last name"
  @data = data.sort_by.sort { |a, b| b[ln_index] <=> a[ln_index] }
  erb :'data/index.html'
end

