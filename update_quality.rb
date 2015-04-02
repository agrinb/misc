require 'award'
#used Award class to handle award updates

def update_quality(awards)
  awards.each { |award| award.update_award! }
end