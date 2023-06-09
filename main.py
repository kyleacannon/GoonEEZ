import os
import click

# csv_path = '/text.csv'
# phone_number = 1234567899
# send_alerts = True
# alert_cron = '* * * * *'
# #defaults to []


@click.group()
#options here are for config and overall cli settings
def cli():
    """Welcome to GoonEEZ"""
#
# @cli.group()
# def task_creation():
#     pass
#
# @cli.group()
# def project_creation():
#     pass
#
# @cli.group()
# def conditional_creation():
#     pass

#TODO
# EDIT TEXT PROMPT AND HELPS
# MENU COMMAND
# INPUT VALIDATION
# CALLBACKS FOR QUERIES
# CHOICE FOR ARGUMENTS


@cli.command()
@click.argument('type', type=str)
@click.option('-rt', '--rating', 'rating', prompt='what is the rating: ', type=int, help='specify a rating for the task you create, used for sorting and statistics')
@click.option('-cond', '--conditional', 'conditional', is_flag=True, default=False, show_default=True, help='schedule an item, in a specified area, to be created upon completion of another item')
def create(type, rating, conditional):
    """tasks(task), projects(project), or a shopping list(shop)"""
    click.echo(f'type={type} rating={rating}')


@cli.command()
@click.option('-s', '--search', 'search', prompt='what is the name of the item you want to complete: ', help='specify a rating for the task you create, used for sorting and statistics')
def complete(search):
    """search for an item to complete"""
    click.echo(f'complete search for "{search}"')


@cli.command()
@click.argument('type', type=str)
def view(type):
    """everything(all), tasks(tasks), projects(projects), or your shopping list(shops)"""
    click.echo(f'view {type}')


# shortcut if you have pk
@cli.command()
@click.option('-s', '--search', 'search', prompt='what is the name of the item you want edit to complete: ', help='specify a rating for the task you create, used for sorting and statistics')
def edit(search):
    """search for an item to edit"""
    click.echo(f'edit search for "{search}"')


# shortcut if you have pk
@cli.command()
@click.option('-s', '--search', 'search', prompt='what is the name of the item you want edit to complete: ', help='specify a rating for the task you create, used for sorting and statistics')
def delete(search):
    """search for an item to delete"""
    click.echo(f'delete search for "{search}"')


@cli.command()
@click.argument('function', type=str,)
def alerts(function):
    """re-configure alerts(config), enable alerts(enable), disable alerts(disable)"""
    click.echo(f'alerts with {function}')



@cli.command()
def stats():
    """see your progress with math and dashboards"""
    click.echo(f'run stats math and charts')


if __name__ == '__main__':
    cli()



#WHITE SPACE
# MORE WHITE SPACE