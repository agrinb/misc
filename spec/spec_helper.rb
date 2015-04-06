require 'sinatra'
require 'rspec'
require 'capybara/rspec'
require 'capybara/dsl'

@test_url = "test"

RSpec.configure do |config|
  config.include Capybara::DSL
end

Capybara.configure do |config|
  config.run_server = false
  config.current_driver = :selenium
  config.app = "DataConverter"
  config.app_host = "http://localhost:4567"

  # config.include Capybara::DSL, feature: true
  # config.include Capybara::RSpecMatchers, feature: true
end