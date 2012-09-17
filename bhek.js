var links = [];
var casper = require('casper').create();
var padding=casper.cli.get(0)

function getLinks() {
   
    var links = document.querySelectorAll('h3.r a');
    return Array.prototype.map.call(links, function(e) {
        return e.getAttribute('href')
    });
}


casper.start();

casper.open('https://www.google.com/search?q=inurl:%27bhadmin.php%27&hl=fr&safe=off&client=firefox-a&start='+padding+'&rls=org.mozilla:fr:official&biw=1366&bih=656&prmd=imvns&filter=0')
casper.then(function() {
    // aggregate results for the 'casperjs' search
    links = this.evaluate(getLinks);
	
    // now search for 'phantomjs' by filling the form again
});



casper.run(function() {
    // echo results in some pretty fashion
    this.echo(links.length + ' links found:');
    this.echo(' - ' + links.join('\n - ')).exit();
});
