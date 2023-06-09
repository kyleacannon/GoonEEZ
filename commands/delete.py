def delete_step():
# item_name = input(f"what is the the name of the item you would like to delete \n")
# if item_name== exit
#     return
# #QUERY WITH ITEM NAME
# if records pulled length is longer than one
#     show all records
#     ask which one is the correct one to delete
#     choose from index provided and store hash
# else:
# #meaning the records pulled has lenght of one
#     take the pk, hash, identifier, of index 0
        verify input from user
        delete the record with hash, identifier
        return

if found nothing
# we could not find a item with the name that name retry or type exit to leave
#loop


@click.group()
def cli():
        """Welcome to goonez"""
        pass

@click.command()
def create():
        click.echo('create')

@click.command()
def delete():
        click.echo('delete')

cli.add_command(create)
cli.add_command(delete)

if __name__ == '__main__':
        cli()
