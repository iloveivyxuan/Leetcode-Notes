class WordDistance

=begin
    :type words: String[]
=end
    def initialize(words)
        @size = words.size
        @hash = Hash.new { |hash, key| hash[key] = [] }
        words.each_with_index { |word, index| @hash[word] << index }
    end


=begin
    :type word1: String
    :type word2: String
    :rtype: Integer
=end
    def shortest(word1, word2)
        word1_indices = @hash[word1]
        word2_indices = @hash[word2]

        dis = @size
        i, j = 0, 0
        while word1_indices[i] && word2_indices[j]
            dis = [dis, (word1_indices[i] - word2_indices[j]).abs].min
            if word1_indices[i] < word2_indices[j]
                i += 1
            else
                j += 1
            end
        end

        return dis
    end


end

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance.new(words)
# param_1 = obj.shortest(word1, word2)
