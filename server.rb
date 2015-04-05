require 'sinatra'
require 'pry'
require 'sinatra/reloader'
require 'csv'


Dir.foreach('/data') do |file|
  csv_for_each(file)
end

def csv_for_each(file)

  CSV.foreach(file) do |row|
    ary << row
  end
end



Dir.foreach('*.txt') do |file|
  csv_row = []
  CSV.open(file, "w", {:col_sep => "\t"}) do |row|
  csv_row << row
  csv_file =  File.open('/data/combined_output.csv', 'a'}
  File.write(csv_file, csv_row)
  csv_file.close
end





#==============================================================================
get '/test' do
  @title = "Launch Academy Movies"
  @page_title = "All Actors"
  
  erb :'actors/actors'
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

get '/actors/:id' do
  actor_info = get_actor_info(params[:id])

  @page_title = actor_info[0]["name"]
  @title = @page_title

  @actor_movies = get_actor_info(params[:id])

  # @actor_movies = get_movie_titles(actor_info)

  erb :'actors/show.html'
end

get '/movies' do
  @title = "Movies"
  @page_title = "Movies"
  @movie_data = find_movie_det
  erb :'movies/index.html'
end

get '/movies/new' do
  @genres_list = genres_list
  @studios_list = studios_list
  erb :'movies/new.html'
end

get '/movies/:id' do
  @movie_details = find_movie_details(params[:id])
  @movie_actors = find_movie_actors(params[:id])
  @page_title = @movie_details.first["title"]
  erb :'movies/show.html'
end



post '/movies/new' do
  binding.pry
  studio_id = find_studio_id(params[:studio_name])
  genre_id = find_genre_id(params[:genre_name])
  submit_new_movie(params[:movie_title], params[:release_year], params[:rating], genre_id, studio_id)
  redirect '/movies'
end


