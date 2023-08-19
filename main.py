import os
import click
import psycopg2
import commands

# TODO
# connection and config module
# finish logic
# redundancy -- module seperation
# parse sql return
# test document
# package
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
@click.option('-rt', '--rating', 'rating', prompt='what is the rating: ', type=int, help='specify a rating for the task you create, used for sorting and statistics')
# @click.option('-cond', '--conditional', 'conditional', is_flag=True, default=False, show_default=True, help='schedule an item, in a specified area, to be created upon completion of another item')
@click.option('-dsc', '--description', 'description', prompt='what is the description: ', type=str, help='specify a description for the task you create, used for listing and id purposes')
def create(type, name, rating, conditional, description):
    """tasks(task), projects(project), or a shopping list(shop)"""
    click.echo(f'type={type} name={name} rating={rating} description={description}')
    commands.create.create_step(type, name, rating, description)


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
            pass
            for record in results:
                print(f'Tag:{record[0]} Name:{record[2]} Desc: {record[4]} \n')
            tag = input(f'Which record are you searching for? Enter only the tag number.')
            commands.complete.completeStep(tag)
        else:
            tag = results[0][0]
            commands.complete.completeStep(tag)


@cli.command()
@click.argument('type', type=str)
@click.argument('param', type=str)
@click.option('-t', '--tag', 'tag', is_flag=True, default=False, show_default=True, help='specify that you are providing a tag to search by')
def view(type):
    """everything(all), tasks(tasks), projects(projects), or your shopping list(shops)"""
    #SAME THING JUST PRINT
    if tag:
        results = commands.complete.completeStep(tag)
        #complete task
    else:
        results = commands.search.searchParam(type, param)
        if len(results) > 1:
            pass
            # show results
            # prompt which task would yo ulike to complee
            #copy index of prompt
            #complete task
        else:
            pass
            # take tag
            #complete task


# shortcut if you have pk
@cli.command()
@click.argument('type', type=str)
@click.argument('param', type=str)
@click.option('-t', '--tag', 'tag', is_flag=True, default=False, show_default=True, help='specify that you are providing a tag to search by')
def delete(type, param, tag):
    """search for an item to delete"""
    # same but DELETE
    if tag:
        results = commands.complete.completeStep(tag)
        #complete task
    else:
        results = commands.search.searchParam(type, param)
        if len(results) > 1:
            pass
            # show results
            # prompt which task would yo ulike to complee
            #copy index of prompt
            #complete task
        else:
            pass
            # take tag
            #complete task


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
