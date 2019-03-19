import click
import requests
API_KEY = '42ce18fdf501446b923ec8d3f71e6651'

@click.group()
def main():
        """
        NewsAPI is a news application that offers the user 4 sources where she/he is desires to choose any one .
        your choice will returns a list of the top 10 headlines,
        The news headline has a title, description and a url in case the user needs to follow up
        The user also needs to have a valid news api created from http://www.newsapi.org
        """
        pass

@main.command()

def listsources():
	""" Lists 4 sources from the API """
	main_url = " https://newsapi.org/v2/sources?apiKey=42ce18fdf501446b923ec8d3f71e6651"

	
	open_source = requests.get(main_url).json() 

	
	source = open_source["sources"] 

	 
	results = [] 
	
	for news in source: 
                results.append(news["id"])
            
   	
	for current_news in results[0:4]:
             print(current_news)	


@main.command()
def topheadlines():
          """ enter your choice from the listsources """
          newsSource = click.prompt("Enter your choice from listsources")
    
          main_url = "https://newsapi.org/v2/top-headlines?apiKey=42ce18fdf501446b923ec8d3f71e6651source="+newsSource

	
          open_headline = requests.get(main_url).json() 

	
          headline = open_headline["articles"] 

	
	 
          output = [] 
	
          for top_news in headline: 
                click.echo('\n')
                click.secho(click.style('TITLE: ' + top_news['title'], fg='yellow'))
                click.secho(click.wrap_text(top_news['description']))
                click.secho(click.style('DOMAIN: ' + top_news['url'], fg='red'))
           
           	
          for choice in output[:11]:
                print(choice)


if __name__ == '__main__':
    main()
print(__name__)