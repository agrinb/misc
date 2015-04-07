require 'sinatra'
require "capybara/rspec"
require 'capybara/dsl'
require 'rspec'


Capybara.app = Sinatra::Application

RSpec.configure do |c|
  c.before feature: true do
    self.app = Sinatra::Application
  end

  c.include Capybara::DSL, feature: true
  c.include Capybara::RSpecMatchers, feature: true
end

Capybara.configure do |config|
  config.run_server = false
  config.current_driver = :rack_test
  config.app = Sinatra::Application
  config.app_host = "http://localhost:4567"
end

