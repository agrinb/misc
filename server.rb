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
  unless /([0-9]+)\/([0-9]+)\/([0-9]+)/.match(row[-1])
    row[-1], row[-2] = row[-2], row[-1]
  end
  if row.length < 6
    row.insert(2, nil)
  end
  p row
  arr << row
end 

data = arr

SurnameIndex = 0
GenderIndex  = 3
DateIndex    = 5

#==============================================================================
get '/test' do
  @title = "Launch Academy Movies"
  @page_title = "All Actors"
  
  erb :'actors/actors'
end

get '/genres_then_surname' do
  @data = data.sort_by.sort_by { |object| [ object[GenderIndex], object[SurnameIndex] ] }.inspect
end

get '/birth_date' do
  #binding.pry
  @data = data.sort_by.sort_by do |object| 
    Date.strptime(object[DateIndex], '%m/%d/%Y') 
  end
  erb :'actors/date.html'
end

get '/last_name' do
  @data = data.sort_by.sort { |a, b| b[SurnameIndex] <=> a[SurnameIndex] }.inspect
end



get '/' do
  @page_title = "WELCOME TO THE  FD H  LAUNCH ACADEMYY MOVIE LIST!1!11!ONE!"
  erb :index
end

get '/actors' do
  @title = "Launch Academy Movies"
  @page_title = "All Actors"
  @actors = db_connection do |conn|
              conn.exec('SELECT actors.name, actors.id FROM actors ORDER BY actors.name')
            end
  erb :'actors/actors'
end

# get '/actors/:id' do
#   actor_info = get_actor_info(params[:id])

#   @page_title = actor_info[0]["name"]
#   @title = @page_title

#   @actor_movies = get_actor_info(params[:id])

#   # @actor_movies = get_movie_titles(actor_info)

#   erb :'actors/show.html'
# end

# get '/movies' do
#   @title = "Movies"
#   @page_title = "Movies"
#   @movie_data = find_movie_det
#   erb :'movies/index.html'
# end

# get '/movies/new' do
#   @genres_list = genres_list
#   @studios_list = studios_list
#   erb :'movies/new.html'
# end

# get '/movies/:id' do
#   @movie_details = find_movie_details(params[:id])
#   @movie_actors = find_movie_actors(params[:id])
#   @page_title = @movie_details.first["title"]
#   erb :'movies/show.html'
# end



# post '/movies/new' do
#   binding.pry
#   studio_id = find_studio_id(params[:studio_name])
#   genre_id = find_genre_id(params[:genre_name])
#   submit_new_movie(params[:movie_title], params[:release_year], params[:rating], genre_id, studio_id)
#   redirect '/movies'
# end


