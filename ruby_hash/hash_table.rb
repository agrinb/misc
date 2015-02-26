require 'pry'
require_relative 'hash_entry.rb'

class Hash_me
  attr_accessor :bin_count, :bins

  def initialize
    self.bin_count = 500
    self.bins = Array.new 
  end


  def add(key, value)
    index = bin_for(key)
    self.bins[index] ||= []
    self.bins[index] << [key, value]
  end

  def evl(key)
    index = bin_for(key)
    bin = self.bins[index].detect do |entry|
      entry[0] == key
    end
    bin[1]
  end

  def merge(entry)
    entry.bins.each_with_index do |sub,i|
      if self.bins[i] == nil
        self.bins[i] = sub
      else
        add(sub[0],sub[1])
      end
    end
    self
  end

  def keys
    self.bins.select! do |x|
      next if x == nil
      x[0]
     end
  end



  private
  def bin_for(key)
    key.hash % self.bin_count
  end

end