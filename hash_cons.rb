require 'pry'


def start hash, arr
  hkey = arr.shift.to_s
  if hash[hkey].is_a? Hash # if hash has a key that is associated with array 
    start(hash[hkey], arr) #recurse with moded array
  elsif arr.size == 0  # if array is on it's last variable
    if hash.keys.include?(hkey)
      child = hash[hkey] +=1
    else 
      hash.merge!({hkey => 1}) # insert +1
    end
  else#it does not have a key that is associated with the array 
    hash.merge!({hkey => {}})  # create a hash with an empty hash value
    start(hash[hkey], arr)
  end
  hash
end


