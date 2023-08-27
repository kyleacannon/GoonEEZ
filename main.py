import os
import click
import psycopg2
import commands.create
import commands.search
import commands.view
import commands.delete
import commands.complete

# TODO
# finish logic
# redundancy -- module seperation
# case insensitivity
# parse results
# connection and config module
# parse sql return
# test document
# package
# seperate connection from modules
# TODO AFTER FUNCTION
# PRINT TO TXT
# HAVE BUDGET
# APPEND TO SCHEDULE
# CONFIG
# DOCKER
# GITHUB
# conditional
# setup error handling
# INPUT VALIDATION
# Menu
# data stats/sosby

@click.group()
#options here are for config and overall cli settings
def cli():
    """Welcome to GoonEEZ"""

@cli.command()
@click.argument('type', type=str)
@click.argument('name', type=str)
@click.option('-rt', '--rating', 'rating', prompt='How is important is this task on a scale of 1-10?', type=int, help='specify a rating for the task you create, used for sorting and statistics')
# @click.option('-cond', '--conditional', 'conditional', is_flag=True, default=False, show_default=True, help='schedule an item, in a specified area, to be created upon completion of another item')
@click.option('-dsc', '--description', 'description', prompt='what is the description: ', type=str, help='specify a description for the task you create, used for listing and id purposes')
def create(type, name, rating, description):
    """tasks(task), projects(project), or a shopping list(shop)"""
    commands.create.createStep(type, name, rating, description)


@cli.command()
@click.argument('type', type=str)
@click.argument('param', type=str)
@click.option('-t', '--tag', 'tag', is_flag=True, default=False, show_default=True, help='specify that you are providing a tag to search by')
def complete(type, param, tag):
    """search for an item to complete"""
    if tag:
        commands.complete.completeStep(tag)
    else:
        results = commands.search.searchParam(type, param)
        if len(results) > 1:
            for record in results:
                print(f'Tag:{record[0]} Name:{record[2]} Desc: {record[4]} \n')
            tag = input(f'Which record are you searching for? Enter only the tag number.')
            commands.complete.completeStep(tag)
        else:
            tag = results[0][0]
            commands.complete.completeStep(tag)


@cli.command()
@click.argument('type', type=str)
@click.option('-t', '--tag', 'tag', is_flag=True, default=False, show_default=True, help='specify that you are providing a tag to search by')
#SHOW COMPLETED FLAG
#@click.option('-c', '--completed', 'completed', is_flag=True, default=False, show_default=True, help='flag to indicate the search to retun completed items as well'
def view(type, tag):
    """everything(all), tasks(task), projects(project), or your shopping list(shop)"""
    if tag:
        results = commands.search.searchSpec(tag)
        print(results)
    else:
        results = commands.search.searchTypes(type)
        print(results)


# shortcut if you have pk
@cli.command()
@click.argument('type', type=str)
@click.argument('param', type=str)
@click.option('-t', '--tag', 'tag', is_flag=True, default=False, show_default=True, help='specify that you are providing a tag to search by')
#SHOW COMPLETED FLAG
#@click.option('-c', '--completed', 'completed', is_flag=True, default=False, show_default=True, help='flag to indicate the search to retun completed items as well'
def delete(type, param, tag):
    """search for an item to delete"""
    if tag:
        results = commands.delete.deleteStep(tag)
        print(results)
    else:
        results = commands.search.searchParam(type, param)
        if len(results) > 1:
            for record in results:
                print(f'Tag:{record[0]} Name:{record[2]} Desc: {record[4]} \n')
            tag = input(f'Which record are you searching for? Enter only the tag number.')
            commands.delete.deleteStep(tag)
        else:
            tag = results[0][0]
            commands.delete.deleteStep(tag)

# @cli.command()
# @click.argument('function', type=str,)
# def alerts(function):
#     """re-configure alerts(config), enable alerts(enable), disable alerts(disable)"""
#     click.echo(f'alerts with {function}')
#
#
# @cli.command()
# def stats():
#     """see your progress with math and dashboards"""
#     click.echo(f'run stats math and charts')


if __name__ == '__main__':
    cli()
