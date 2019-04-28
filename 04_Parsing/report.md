# REPORT #

## Part 1 - UDPipe ##

I diffed the first ten trees between fr\_sequoia-ud-test.conllu and the output
of the parsing of this file found in fr\_udpipe\_test.conllu and stored the
results in a file called test.diff.  I got back some output, meaning there are
some differences between these trees, but when looking over I found that the
syntactic categories of the colliding words were all the same. The columns
detailing morphologically derived information, such as person and number, are
consistent, but the syntactically derived information, meaning the dependency
trees, are distinct. These two analyses of the sentences may both be correct,
but they are nontheless dictinct from eachother.

## Part 2 - Word Order ##

I ended up evaluating 12 treebanks in for this one, Basque, Breton, Catalan,
Danish, English, a Hindi-English code switching treebank, Hindi, French, Greek,
Serbian, Slovak, and Uyghur. Most of them were chosen more or less at random,
but some of them show interesting results. There is a rather marked difference
between the numbers gotten from the Slovak treebank and the Serbian treebank.
This may indicate a difference in word order tendencies between West Slavic and
South Slavic languages. The numbers gotten from the English, Hindi-English, and
Hindi treebank show the effects of code switching on the word order tendencies
of speakers, so that's pretty cool.
