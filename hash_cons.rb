require 'pry'


def start hash, arr
  binding.pry
  hkey = arr.shift.to_s
  if hash[hkey].is_a? Hash # if hash has a key that is associated with array 
    binding.pry
    start(hash[hkey], arr) #recurse with moded array
  elsif arr.size == 0  # if array is on it's last variable
    binding.pry
    if hash.keys.include?(hkey)
      child = hash[hkey] +=1
    else 
      hash.merge!({hkey => 1}) # insert +1
    end
  else#it does not have a key that is associated with the array 
    binding.pry
    hash.merge!({hkey => {}})  # create a hash with an empty hash value
    start(hash[hkey], arr)
  end
  hash
end



hash = {'a' => {'b' => { 'g' => 1}}}
hash2 =  start(hash, arr)
p start(hash2, arr2)


