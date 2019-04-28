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


