# Inverted-Index-API

This is an Inverted-Index API that stores data like how ElasticSearch stores data. The data can be searched very effectively at a faster time.

It takes in multiple paragraphs of text, and assigns a unique ID To each paragraph and stores the words to paragraph mappings on an inverted index. This is similar to what elasticsearch does. This paragraph can also be referred to as a ‘document’

Given a word to search for, it lists out the top 10 paragraphs in which the word is present.

Inverted-Index API can do the following 3 things:

- clear - Clear the index and all indexed documents

- index - Index a given document (After having split the input into paragraphs a.k.a document )

- Search - Given a word, search for it and retrieve the top 10 paragraphs (Documents) that contain it

Sample Input:

Two documents (paragraphs) separated by two new lines (\n\n)

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Magna ac placerat vestibulum lectus. Elit duis tristique sollicitudin nibh sit amet commodo. Senectus et netus et malesuada fames. Fermentum iaculis eu non diam phasellus vestibulum lorem sed. Dictumst quisque sagittis purus sit amet volutpat consequat mauris. Aliquam ut porttitor leo a diam sollicitudin tempor. Consectetur a erat nam at lectus urna duis convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque. 



Maecenas volutpat blandit aliquam etiam erat velit scelerisque. Lectus sit amet est placerat in egestas erat imperdiet. Ante in nibh mauris cursus mattis. Tellus rutrum tellus pellentesque eu tincidunt. Euismod quis viverra nibh cras pulvinar mattis. Proin nibh nisl condimentum id venenatis a. Quam elementum pulvinar etiam non quam. Arcu dictum varius duis at consectetur lorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id.

Sample search

    Input - lorem

        Results: Paragraph 1 and 2 are returned

    Input - Maecenas

        Results: Paragraph 1
