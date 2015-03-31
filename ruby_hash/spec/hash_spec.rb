require_relative '../hash_table.rb'
require 'pry'

RSpec.describe hash do
  context "when you initialize a hash" do
    it "it returns a hash object" do
      hash = Hash_me.new
      expect(hash).to be_a(Hash_me)
    end

    it "accepts initilization of an even member list" do
    end

    it "can only accept an even amount of arguments" do
    end
  end

  context "instance methods" do
    it "returns value when key is supplied" do
      hash_me = Hash_me.new
      hash_me.add(1,2)
      expect(hash_me.evl(1)).to eq(2)
    end

    it "merges other hashes into itself" do 
      hash_me = Hash_me.new
      ha1 = hash_me.add(2,3)
      hash_me2 = Hash_me.new
      ha2 = hash_me2.add(4,5)
      expect(hash_me.merge(hash_me2)).to be_a(Hash_me)
      expect(hash_me.evl(4)).to eq(5)
      expect(hash_me.evl(2)).to eq(3) 
    end

    it "returns array of keys" do
      hash_me = Hash_me.new
      h = hash_me.add(2,3)
      h = h.add(4,5)
      expect(h.keys).to match_array([2,4])
    end

    it "returns array of values" do
      hash_me = Hash_me.new
      h = hash_me.add(2,3)
      h = h.add(4,5)
      expect(h.values).to match_array([3,5])
    end


  end
end
